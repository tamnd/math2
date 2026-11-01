---
records:
    - id: N4HRP6SQS6
      kind: monograph
      title: Understanding Analysis
      creators:
        - name: Stephen Abbott
          role: author
      date: "2001"
      msc:
        - code: 26-01
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "2001"
          ids:
            doi:
                - 10.1007/978-0-387-21506-8
                - 10.1007/978-1-4939-2712-8
            zbl: "0966.26001"
            zbl_id: "1571468"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer New York
              date: "2001"
              ids:
                isbn:
                    - "9781441928665"
                    - "9780387215068"
              access:
                class: record
            - key: m2
              kind: print
              publisher: Springer New York
              date: "2015"
              ids:
                isbn:
                    - "9781493927111"
                    - "9781493927128"
              access:
                class: record
      relations:
        - kind: part_of
          to: NWQC4TW7S9
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 v0.6.16 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-0-387-21506-8
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4939-2712-8
          level: work
        - source: zbmath_search
          snapshot: blake3:928c873c1dac6852b2bf2c77184182759305f81342a4dc8ca5c0d4768bc6dd1e
          native_id: "1571468"
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
