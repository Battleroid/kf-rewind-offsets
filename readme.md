# kf-rewind-offsets

Rewind or set offsets for a consumer group. Valid values should be whatever pykafka's simple consumer [`reset_offsets`][0] func takes.

For example: a valid timestamp, offset, or in this case a negative value (default of -1000) which will be subtracted from the current consumer offset. If you supply -100 and the current offset is 500, then the offset will (should) be reset to 400.

Offset values set to far in the future for a partition will not be included in the offset request, you will see these as messages notifying you that they were skipped (with a diff how ahead they were). 

# example usage


```bash
$ rewind-offsets something something-group -- -1000

Do these offset requests look right to you?

   0: 575541998 => 575540998 (diff of 1000)
   1: 575556540 => 575555540 (diff of 1000)
   2: 575571258 => 575570258 (diff of 1000)
   3: 575554963 => 575553963 (diff of 1000)
   4: 575541343 => 575540343 (diff of 1000)
   5: 575547849 => 575546849 (diff of 1000)
   6: 575530694 => 575529694 (diff of 1000)
   7: 575562615 => 575561615 (diff of 1000)
   8: 575546198 => 575545198 (diff of 1000)
   9: 575546865 => 575545865 (diff of 1000)
  10: 575570663 => 575569663 (diff of 1000)
  11: 575551983 => 575550983 (diff of 1000)
  12: 575555787 => 575554787 (diff of 1000)
  13: 575569575 => 575568575 (diff of 1000)
  14: 575566993 => 575565993 (diff of 1000)
  15: 575528108 => 575527108 (diff of 1000)
  16: 575510533 => 575509533 (diff of 1000)
  17: 575564411 => 575563411 (diff of 1000)
  18: 575538292 => 575537292 (diff of 1000)
  19: 575569197 => 575568197 (diff of 1000)
  20: 575545021 => 575544021 (diff of 1000)
  21: 575589558 => 575588558 (diff of 1000)
  22: 575561008 => 575560008 (diff of 1000)
  23: 575529961 => 575528961 (diff of 1000)
  24: 575563580 => 575562580 (diff of 1000)
  25: 575548302 => 575547302 (diff of 1000)
  26: 575536140 => 575535140 (diff of 1000)
  27: 575551226 => 575550226 (diff of 1000)
  28: 575500174 => 575499174 (diff of 1000)
  29: 575547944 => 575546944 (diff of 1000)
  30: 575518283 => 575517283 (diff of 1000)
  31: 575551569 => 575550569 (diff of 1000)

Continue with reset? [y/N]: N
```

[0]: http://pykafka.readthedocs.io/en/latest/api/simpleconsumer.html#pykafka.simpleconsumer.SimpleConsumer.reset_offsets
