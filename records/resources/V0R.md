---
records:
    - id: V0R5E1VR15
      kind: monograph
      title: Probability Theory II
      creators:
        - name: Michel Loève
          role: author
      date: "1977"
      expressions:
        - key: e1
          kind: edition
          date: "1977"
          ids:
            doi:
                - 10.1007/978-1-4612-6257-2
                - 10.1007/978-1-4684-9464-8
                - 10.1007/978-1-4757-6288-4
          manifestations:
            - key: m1
              kind: print
              publisher: Springer New York
              date: "1978"
              ids:
                isbn:
                    - "9780387943589"
                    - "9781461262572"
            - key: m2
              kind: print
              publisher: Springer New York
              date: "1977"
              ids:
                isbn:
                    - "9781468494662"
                    - "9781468494648"
            - key: m3
              kind: print
              publisher: Springer New York
              date: "1977"
              ids:
                isbn:
                    - "9780387901275"
                    - "9781475762884"
      relations:
        - kind: part_of
          to: 7ME1ABA6H5
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.2 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4612-6257-2
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4684-9464-8
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4757-6288-4
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
