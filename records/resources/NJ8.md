---
records:
    - id: NJ8MZ098DC
      kind: monograph
      title: Undergraduate Analysis
      creators:
        - name: Serge Lang
          role: author
      date: "1983"
      msc:
        - code: 46G05
          from: zbmath_search
        - code: 46-01
          from: zbmath_search
        - code: 26-01
          from: zbmath_search
        - code: "26E15"
          from: zbmath_search
        - code: "26E20"
          from: zbmath_search
        - code: 34G10
          from: zbmath_search
        - code: 42A16
          from: zbmath_search
        - code: 42A38
          from: zbmath_search
        - code: 26B20
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "1983"
          ids:
            doi:
                - 10.1007/978-1-4757-1801-0
                - 10.1007/978-1-4757-2698-5
            zbl: "0509.46037"
            zbl_id: "3804205"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer New York
              date: "1983"
              ids:
                isbn:
                    - "9781475718034"
                    - "9781475718010"
              access:
                class: record
            - key: m2
              kind: print
              publisher: Springer New York
              date: "1997"
              ids:
                isbn:
                    - "9781441928535"
                    - "9781475726985"
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
          native_id: 10.1007/978-1-4757-1801-0
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4757-2698-5
          level: work
        - source: zbmath_search
          snapshot: blake3:928c873c1dac6852b2bf2c77184182759305f81342a4dc8ca5c0d4768bc6dd1e
          native_id: "3804205"
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
          by: m2 v0.6.14 scope/1
          note: from in to in
---
