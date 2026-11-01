---
records:
    - id: YNTWFVM3Q9
      kind: monograph
      title: A First Course in Noncommutative Rings
      creators:
        - name: T. Y. Lam
          role: author
      date: "1991"
      msc:
        - code: 16-01
          from: zbmath_search
        - code: 16D70
          from: zbmath_search
        - code: 16D60
          from: zbmath_search
        - code: 16L30
          from: zbmath_search
        - code: 16W60
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "1991"
          ids:
            doi:
                - 10.1007/978-1-4419-8616-0
                - 10.1007/978-1-4684-0406-7
            zbl: "0728.16001"
            zbl_id: "49937"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer New York
              date: "2001"
              ids:
                isbn:
                    - "9780387953250"
                    - "9781441986160"
              access:
                class: record
            - key: m2
              kind: print
              publisher: Springer US
              date: "1991"
              ids:
                isbn:
                    - "9781468404081"
                    - "9781468404067"
              access:
                class: record
      relations:
        - kind: part_of
          to: 7ME1ABA6H5
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 v0.6.13 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4419-8616-0
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4684-0406-7
          level: work
        - source: zbmath_search
          snapshot: blake3:a8e1c9c763cc4a7cf0816f17b1654f8f6ec07d6faeb609dc93b9b617c8b4e7e4
          native_id: "49937"
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
