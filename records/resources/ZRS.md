---
records:
    - id: ZRSMHPSCXF
      kind: monograph
      title: Geometrical Methods in the Theory of Ordinary Differential Equations
      creators:
        - name: V. I. Arnold
          role: author
      date: "1983"
      msc:
        - code: 34-01
          from: zbmath_search
        - code: 58-01
          from: zbmath_search
        - code: 34D30
          from: zbmath_search
        - code: 37C75
          from: zbmath_search
        - code: 34C29
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "1983"
          ids:
            doi:
                - 10.1007/978-1-4612-1037-5
                - 10.1007/978-1-4684-0147-9
            zbl: "0507.34003"
            zbl_id: "3800064"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer New York
              date: "1988"
              ids:
                isbn:
                    - "9781461269946"
                    - "9781461210375"
              access:
                class: record
            - key: m2
              kind: print
              publisher: Springer US
              date: "1983"
              ids:
                isbn:
                    - "9781468401493"
                    - "9781468401479"
              access:
                class: record
      relations:
        - kind: part_of
          to: GQFCNY816R
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.7 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4612-1037-5
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4684-0147-9
          level: work
        - source: zbmath_search
          snapshot: blake3:a8e1c9c763cc4a7cf0816f17b1654f8f6ec07d6faeb609dc93b9b617c8b4e7e4
          native_id: "3800064"
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
