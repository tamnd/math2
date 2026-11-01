---
records:
    - id: 5ZGMWPE4JE
      kind: monograph
      title: Boundary Integral Equations
      creators:
        - name: George C. Hsiao
          role: author
        - name: Wolfgang L. Wendland
          role: author
      date: "2008"
      msc:
        - code: 65N38
          from: zbmath_search
        - code: 65-02
          from: zbmath_search
        - code: 35J25
          from: zbmath_search
        - code: 65N12
          from: zbmath_search
        - code: 31A10
          from: zbmath_search
        - code: 31B10
          from: zbmath_search
        - code: 35C15
          from: zbmath_search
        - code: 35S15
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "2008"
          ids:
            doi:
                - 10.1007/978-3-030-71127-6
                - 10.1007/978-3-540-68545-6
            zbl: "1157.65066"
            zbl_id: "5288573"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer International Publishing
              date: "2021"
              ids:
                isbn:
                    - "9783030711269"
                    - "9783030711276"
              access:
                class: record
            - key: m2
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "2008"
              ids:
                isbn:
                    - "9783540152842"
                    - "9783540685456"
              access:
                class: record
      relations:
        - kind: part_of
          to: 2M0N86YNGA
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 v0.6.16 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-3-030-71127-6
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-3-540-68545-6
          level: work
        - source: zbmath_search
          snapshot: blake3:928c873c1dac6852b2bf2c77184182759305f81342a4dc8ca5c0d4768bc6dd1e
          native_id: "5288573"
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
