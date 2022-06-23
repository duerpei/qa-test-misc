#/bin/bash

          if ./asyncqueue-test; then echo 'TEST-1 OK'; else echo 'TEST-1 FAIL'; fi; \
          if ./atomic-test; then echo 'TEST-2 OK'; else echo 'TEST-2 FAIL'; fi; \
          if ./bit-test; then echo 'TEST-3 OK'; else echo 'TEST-3 FAIL'; fi; \
          if ./child-test; then echo 'TEST-4 OK'; else echo 'TEST-4 FAIL'; fi; \
          if ./completion-test; then echo 'TEST-5 OK'; else echo 'TEST-5 FAIL'; fi; \
          if ./datetime; then echo 'TEST-6 OK'; else echo 'TEST-6 FAIL'; fi; \
          if ./dirname-test; then echo 'TEST-7 OK'; else echo 'TEST-7 FAIL'; fi; \
          if ./env-test; then echo 'TEST-8 OK'; else echo 'TEST-8 FAIL'; fi; \
          if ./file-test; then echo 'TEST-9 OK'; else echo 'TEST-9 FAIL'; fi; \
          if ./gio-test; then echo 'TEST-10 OK'; else echo 'TEST-10 FAIL'; fi; \
          if ./mainloop-test; then echo 'TEST-11 OK'; else echo 'TEST-11 FAIL'; fi; \
          if ./mapping-test; then echo 'TEST-12 OK'; else echo 'TEST-12 FAIL'; fi; \
          export LD_LIBRARY_PATH=$BOARD_TESTDIR/fuego.$TESTDIR:$PATH/tests:$LD_LIBRARY_PATH; \
          if ./module-test; then echo 'TEST-13 OK'; else echo 'TEST-13 FAIL'; fi; \
          if ./onceinit; then echo 'TEST-14 OK'; else echo 'TEST-14 FAIL'; fi; \
          if ./qsort-test; then echo 'TEST-15 OK'; else echo 'TEST-15 FAIL'; fi; \
          if ./relation-test; then echo 'TEST-16 OK'; else echo 'TEST-16 FAIL'; fi; \
          if ./slice-color; then echo 'TEST-17 OK'; else echo 'TEST-17 FAIL'; fi; \
          if ./slice-concurrent; then echo 'TEST-18 OK'; else echo 'TEST-18 FAIL'; fi; \
          if ./slice-test; then echo 'TEST-19 OK'; else echo 'TEST-19 FAIL'; fi; \
          if ./slice-threadinit; then echo 'TEST-20 OK'; else echo 'TEST-20 FAIL'; fi; \
          if ./sources; then echo 'TEST-21 OK'; else echo 'TEST-21 FAIL'; fi; \
          if ./spawn-test; then echo 'TEST-22 OK'; else echo 'TEST-22 FAIL'; fi; \
          if ./testgdate; then echo 'TEST-23 OK'; else echo 'TEST-23 FAIL'; fi; \
          if ./testglib; then echo 'TEST-24 OK'; else echo 'TEST-24 FAIL'; fi; \
          if ./threadpool-test; then echo 'TEST-25 OK'; else echo 'TEST-25 FAIL'; fi; \
          if ./thread-test; then echo 'TEST-26 OK'; else echo 'TEST-26 FAIL'; fi; \
          if ./timeloop; then echo 'TEST-27 OK'; else echo 'TEST-27 FAIL'; fi; \
          if ./type-test; then echo 'TEST-28 OK'; else echo 'TEST-28 FAIL'; fi; \
          if ./unicode-caseconv; then echo 'TEST-29 OK'; else echo 'TEST-29 FAIL'; fi; \
          if ./iochannel-test; then echo 'TEST-30 OK'; else echo 'TEST-30 FAIL'; fi; \
          if ./unicode-caseconv; then echo 'TEST-31 OK'; else echo 'TEST-31 FAIL'; fi; \
          if ./unicode-collate; then echo 'TEST-32 OK'; else echo 'TEST-32 FAIL'; fi; \
          if ./unicode-encoding; then echo 'TEST-33 OK'; else echo 'TEST-33 FAIL'; fi
