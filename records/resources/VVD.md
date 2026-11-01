---
records:
    - id: VVDJP1CNZ8
      kind: monograph
      title: Advanced Linear Algebra
      creators:
        - name: Steven Roman
          role: author
      date: "1992"
      msc:
        - code: 15-02
          from: zbmath_search
        - code: 46C05
          from: zbmath_search
        - code: 47B15
          from: zbmath_search
        - code: 15A06
          from: zbmath_search
        - code: 15A04
          from: zbmath_search
        - code: 16D10
          from: zbmath_search
        - code: 15A18
          from: zbmath_search
        - code: 15A63
          from: zbmath_search
        - code: 15A69
          from: zbmath_search
        - code: 51N10
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "1992"
          ids:
            doi:
                - 10.1007/978-0-387-72831-5
                - 10.1007/978-1-4757-2178-2
            zbl: "0754.15002"
            zbl_id: "54001"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer New York
              date: "2008"
              ids:
                isbn:
                    - "9780387728285"
                    - "9780387728315"
              access:
                class: record
            - key: m2
              kind: print
              publisher: Springer New York
              date: "1992"
              ids:
                isbn:
                    - "9781475721805"
                    - "9781475721782"
              access:
                class: record
      relations:
        - kind: part_of
          to: 7ME1ABA6H5
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 v0.6.14 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-0-387-72831-5
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4757-2178-2
          level: work
        - source: zbmath_search
          snapshot: blake3:c337ce98d6a5f313c8656eac90c3348668181c9ed20fe8fe7554afd8dc3904ca
          native_id: "54001"
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
