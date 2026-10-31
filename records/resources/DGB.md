---
records:
    - id: DGBGBY4FKY
      kind: monograph
      title: Algebra
      creators:
        - name: L. E. Sigler
          role: author
      date: "1976"
      msc:
        - code: 13-01
          from: zbmath_search
        - code: 15-01
          from: zbmath_search
        - code: 13Fxx
          from: zbmath_search
        - code: 13Cxx
          from: zbmath_search
        - code: 20-01
          from: zbmath_search
        - code: 08-01
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "1976"
          ids:
            doi:
                - 10.1007/978-1-4613-9410-5
                - 10.1007/978-3-662-26738-7
            zbl: "0353.13001"
            zbl_id: "3549096"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer New York
              date: "1976"
              ids:
                isbn:
                    - "9781461394129"
                    - "9781461394105"
              access:
                class: record
            - key: m2
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "1976"
              ids:
                isbn:
                    - "9783540901952"
                    - "9783662267387"
              access:
                class: record
      relations:
        - kind: part_of
          to: NWQC4TW7S9
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.7 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4613-9410-5
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-3-662-26738-7
          level: work
        - source: zbmath_search
          snapshot: blake3:a8e1c9c763cc4a7cf0816f17b1654f8f6ec07d6faeb609dc93b9b617c8b4e7e4
          native_id: "3549096"
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
