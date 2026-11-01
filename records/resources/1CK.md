---
records:
    - id: 1CKVDHB724
      kind: monograph
      title: Linear Algebra in Action
      creators:
        - name: Harry Dym
          role: author
      date: "2013-12-31"
      msc:
        - code: 15-01
          from: zbmath_search
        - code: 39-01
          from: zbmath_search
        - code: 34-01
          from: zbmath_search
        - code: 93-01
          from: zbmath_search
        - code: 11-01
          from: zbmath_search
        - code: 52-01
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "2013-12-31"
          ids:
            doi:
                - 10.1090/gsm/078
                - 10.1090/gsm/232
            zbl: "1285.15001"
            zbl_id: "6259850"
          manifestations:
            - key: m1
              kind: print
              publisher: American Mathematical Society
              date: "2013-12-31"
              ids:
                isbn:
                    - "9781470409081"
                    - "9781470414436"
              access:
                class: record
            - key: m2
              kind: print
              publisher: American Mathematical Society
              date: "2023"
              ids:
                isbn:
                    - "9781470474188"
                    - "9781470472061"
                    - "9781470474195"
                    - "9781470477073"
              access:
                class: record
      relations:
        - kind: part_of
          to: YBEDX3XNVA
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 v0.6.13 scope/1
      catalogue:
        - source: ams-series
          snapshot: blake3:caf23f13a44130cfaf0ea65e08f1b670683c2f34af9ccb44343f3bca428b1013
          native_id: 10.1090/gsm/078
          level: work
        - source: ams-series
          snapshot: blake3:caf23f13a44130cfaf0ea65e08f1b670683c2f34af9ccb44343f3bca428b1013
          native_id: 10.1090/gsm/232
          level: work
        - source: zbmath_search
          snapshot: blake3:a8e1c9c763cc4a7cf0816f17b1654f8f6ec07d6faeb609dc93b9b617c8b4e7e4
          native_id: "6259850"
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
