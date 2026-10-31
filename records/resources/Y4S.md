---
records:
    - id: Y4STDVVCT5
      kind: monograph
      title: 'Partial Differential Equations I: Basic Theory'
      creators:
        - name: Michael E. Taylor
          role: author
      date: "2011"
      expressions:
        - key: e1
          kind: edition
          date: "2011"
          ids:
            doi:
                - 10.1007/978-1-4419-7055-8
                - 10.1007/978-3-031-33859-5
          manifestations:
            - key: m1
              kind: print
              publisher: Springer New York
              date: "2011"
              ids:
                isbn:
                    - "9781441970541"
                    - "9781441970558"
            - key: m2
              kind: print
              publisher: Springer International Publishing
              date: "2023"
              ids:
                isbn:
                    - "9783031338588"
                    - "9783031338595"
      relations:
        - kind: part_of
          to: 2M0N86YNGA
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.4 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4419-7055-8
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-3-031-33859-5
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
