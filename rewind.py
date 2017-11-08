import click
from pykafka import KafkaClient


@click.command()
@click.option('--brokers', default='127.0.0.1:9092')
@click.argument('topic')
@click.argument('consumer')
@click.argument('offset', type=int, default=-1000, required=False)
def main(topic, consumer, offset, brokers):
    """Rewind or set offsets for partition(s)"""

    # get clients/consumer
    client = KafkaClient(brokers)
    topic = client.topics[topic.encode('utf-8')]
    consumer = topic.get_simple_consumer(
        consumer_group=consumer.encode('utf-8'), auto_start=False)

    # prep offset reset request
    current_offsets = {c[0]: c[1] for c in consumer.fetch_offsets()}
    fresh_offsets = []
    for p in topic.partitions.values():
        if offset >= 0:
            if offset > current_offsets[p.id].offset:
                diff = abs(offset - current_offsets[p.id].offset)
                click.secho(
                    f'Skipping partition {p.id:2d}, offset is too new (+{diff})',
                    fg='yellow')
                continue
        new_offset = current_offsets[p.id].offset - abs(
            offset) if offset < 0 else offset
        fresh_offsets.append((p, new_offset))

    if not fresh_offsets:
        click.secho('Nothing to reset, aborting')
        raise click.Abort

    # confirm reset
    click.echo(f'Do these offset requests look right to you?\n')
    _fresh_offsets = {
        c[0]: {
            'from': current_offsets[c[0].id].offset,
            'to': c[1]
        }
        for c in fresh_offsets
    }
    for p, val in sorted(_fresh_offsets.items()):
        before = val['from']
        after = val['to']
        diff = abs(before - after)
        click.echo(f'  {p.id:2d}: {before} => {after} (diff of {diff})')
    click.confirm('\nContinue with reset?', abort=True, show_default=True)

    # send request
    consumer.reset_offsets(fresh_offsets)


if __name__ == '__main__':
    main()
