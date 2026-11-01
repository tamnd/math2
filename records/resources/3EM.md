---
records:
    - id: 3EM16DZR2E
      kind: edited-volume
      title: Axiomatic Set Theory
      creators:
        - name: Dana Scott
          role: editor
      date: "1971"
      msc:
        - code: 00B25
          from: zbmath_search
        - code: 03-06
          from: zbmath_search
        - code: 03Exx
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "1971"
          ids:
            doi:
                - 10.1090/pspum/013.1
                - 10.1090/pspum/013.2
            zbl: "0215.32601"
            zbl_id: "3341990"
          manifestations:
            - key: m1
              kind: print
              publisher: American Mathematical Society
              date: "1971"
              ids:
                isbn:
                    - "9780821802458"
                    - "9780821867778"
                    - "9780821892978"
              access:
                class: record
            - key: m2
              kind: print
              publisher: American Mathematical Society
              date: "1974"
              ids:
                isbn:
                    - "9780821802465"
                    - "9780821867785"
                    - "9780821892985"
              access:
                class: record
      relations:
        - kind: part_of
          to: EVG9FMRY3R
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 v0.6.13 scope/1
      catalogue:
        - source: ams-series
          snapshot: blake3:caf23f13a44130cfaf0ea65e08f1b670683c2f34af9ccb44343f3bca428b1013
          native_id: 10.1090/pspum/013.1
          level: work
        - source: ams-series
          snapshot: blake3:caf23f13a44130cfaf0ea65e08f1b670683c2f34af9ccb44343f3bca428b1013
          native_id: 10.1090/pspum/013.2
          level: work
        - source: zbmath_search
          snapshot: blake3:a8e1c9c763cc4a7cf0816f17b1654f8f6ec07d6faeb609dc93b9b617c8b4e7e4
          native_id: "3341990"
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
        - op: scope
          at: "2026-11-01"
          by: m2 v0.6.13 scope/1
          note: from in to in
---
