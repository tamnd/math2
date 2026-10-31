---
records:
    - id: EE0PYM6XDC
      kind: problem-set
      title: Putnam 2011
      date: "2011"
      expressions:
        - key: e1
          kind: edition
          date: "2011"
          structure: EE0PYM6XDC/e1.json
      relations:
        - kind: part_of
          to: TYDZDDC2MA
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.7 scope/1
      catalogue:
        - source: putnam
          snapshot: blake3:317d171d8e409d9741a4f33624a74aedbca628bebf057e16b0f4fee2668a9f1f
          native_id: "2011"
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
    - id: EE0W288D57
      kind: monograph
      title: Numbers and Functions
      creators:
        - name: Victor Moll
          role: author
      date: "2012-09-27"
      msc:
        - code: 00A35
          from: zbmath_search
        - code: 11-01
          from: zbmath_search
        - code: 26A09
          from: zbmath_search
        - code: 33B10
          from: zbmath_search
        - code: 33B15
          from: zbmath_search
        - code: 33C47
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "2012-09-27"
          ids:
            doi: 10.1090/stml/065
            zbl: "1268.00011"
            zbl_id: "6054081"
          manifestations:
            - key: m1
              kind: print
              publisher: American Mathematical Society
              date: "2012-09-27"
              ids:
                isbn:
                    - "9780821891674"
                    - "9780821891667"
                    - "9780821887950"
              access:
                class: record
      relations:
        - kind: part_of
          to: 6RX4VMGQKK
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.7 scope/1
      catalogue:
        - source: ams-series
          snapshot: blake3:caf23f13a44130cfaf0ea65e08f1b670683c2f34af9ccb44343f3bca428b1013
          native_id: 10.1090/stml/065
          level: work
        - source: zbmath_search
          snapshot: blake3:a8e1c9c763cc4a7cf0816f17b1654f8f6ec07d6faeb609dc93b9b617c8b4e7e4
          native_id: "6054081"
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
---
