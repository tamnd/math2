---
records:
    - id: 8GXK1E6NY4
      kind: monograph
      title: Introduction to Analytic Number Theory
      creators:
        - name: Tom M. Apostol
          role: author
      date: "1976"
      msc:
        - code: 11-01
          from: zbmath_search
        - code: 11Axx
          from: zbmath_search
        - code: 11Mxx
          from: zbmath_search
        - code: 11Lxx
          from: zbmath_search
        - code: 11A25
          from: zbmath_search
        - code: 11N37
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "1976"
          ids:
            doi:
                - 10.1007/978-1-4757-5579-4
                - 10.1007/978-3-662-28579-4
            zbl: "0335.10001"
            zbl_id: "3523640"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer New York
              date: "1976"
              ids:
                isbn:
                    - "9781441928054"
                    - "9781475755794"
              access:
                class: record
            - key: m2
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "1976"
              ids:
                isbn:
                    - "9783540901631"
                    - "9783662285794"
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
          native_id: 10.1007/978-1-4757-5579-4
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-3-662-28579-4
          level: work
        - source: zbmath_search
          snapshot: blake3:928c873c1dac6852b2bf2c77184182759305f81342a4dc8ca5c0d4768bc6dd1e
          native_id: "3523640"
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
