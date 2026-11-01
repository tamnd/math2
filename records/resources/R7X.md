---
records:
    - id: R7XZW7ACDM
      kind: edited-volume
      title: Differential Geometry
      creators:
        - name: S. Chern
          role: editor
        - name: R. Osserman
          role: editor
      date: "1975"
      msc:
        - code: 00Bxx
          from: zbmath_search
        - code: 53-06
          from: zbmath_search
        - code: 57-06
          from: zbmath_search
        - code: 55-06
          from: zbmath_search
        - code: 32-06
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "1975"
          ids:
            doi:
                - 10.1090/pspum/027.1
                - 10.1090/pspum/027.2
            zbl: "0304.00009"
            zbl_id: "3475383"
          manifestations:
            - key: m1
              kind: print
              publisher: American Mathematical Society
              date: "1975"
              ids:
                isbn:
                    - "9780821802472"
                    - "9780821867839"
                    - "9780821893135"
              access:
                class: record
            - key: m2
              kind: print
              publisher: American Mathematical Society
              date: "1975"
              ids:
                isbn:
                    - "9780821802489"
                    - "9780821867846"
                    - "9780821893142"
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
          native_id: 10.1090/pspum/027.1
          level: work
        - source: ams-series
          snapshot: blake3:caf23f13a44130cfaf0ea65e08f1b670683c2f34af9ccb44343f3bca428b1013
          native_id: 10.1090/pspum/027.2
          level: work
        - source: zbmath_search
          snapshot: blake3:a8e1c9c763cc4a7cf0816f17b1654f8f6ec07d6faeb609dc93b9b617c8b4e7e4
          native_id: "3475383"
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
