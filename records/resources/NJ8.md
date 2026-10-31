---
records:
    - id: NJ8MZ098DC
      kind: monograph
      title: Undergraduate Analysis
      creators:
        - name: Serge Lang
          role: author
      date: "1983"
      expressions:
        - key: e1
          kind: edition
          date: "1983"
          ids:
            doi:
                - 10.1007/978-1-4757-1801-0
                - 10.1007/978-1-4757-2698-5
          manifestations:
            - key: m1
              kind: print
              publisher: Springer New York
              date: "1983"
              ids:
                isbn:
                    - "9781475718034"
                    - "9781475718010"
            - key: m2
              kind: print
              publisher: Springer New York
              date: "1997"
              ids:
                isbn:
                    - "9781441928535"
                    - "9781475726985"
      relations:
        - kind: part_of
          to: NWQC4TW7S9
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.4 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4757-1801-0
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4757-2698-5
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
