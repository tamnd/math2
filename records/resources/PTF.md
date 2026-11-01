---
records:
    - id: PTFGKZG6B8
      kind: monograph
      title: 'The Geometry of Minkowski Spacetime: An Introduction to the Mathematics of the Special Theory of Relativity'
      creators:
        - name: Gregory L. Naber
          role: author
      date: "1992"
      msc:
        - code: 53Z05
          from: zbmath_search
        - code: 83A05
          from: zbmath_search
        - code: 83C60
          from: zbmath_search
        - code: 83-02
          from: zbmath_search
        - code: 53C50
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "1992"
          ids:
            doi:
                - 10.1007/978-1-4419-7838-7
                - 10.1007/978-1-4757-4326-5
            zbl: "0757.53046"
            zbl_id: "54140"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer New York
              date: "2012"
              ids:
                isbn:
                    - "9781441978370"
                    - "9781441978387"
              access:
                class: record
            - key: m2
              kind: print
              publisher: Springer New York
              date: "1992"
              ids:
                isbn:
                    - "9781441931023"
                    - "9781475743265"
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
          native_id: 10.1007/978-1-4419-7838-7
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4757-4326-5
          level: work
        - source: zbmath_search
          snapshot: blake3:928c873c1dac6852b2bf2c77184182759305f81342a4dc8ca5c0d4768bc6dd1e
          native_id: "54140"
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
