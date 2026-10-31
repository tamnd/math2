---
records:
    - id: 7SDJP7F2YW
      kind: monograph
      title: Linear Functional Analysis
      creators:
        - name: Bryan Patrick Rynne
          role: author
        - name: Martin Alexander Youngson
          role: author
      date: "2000"
      expressions:
        - key: e1
          kind: edition
          date: "2000"
          ids:
            doi:
                - 10.1007/978-1-4471-3655-2
                - 10.1007/978-1-84800-005-6
          manifestations:
            - key: m1
              kind: print
              publisher: Springer London
              date: "2000"
              ids:
                isbn:
                    - "9781852332570"
                    - "9781447136552"
            - key: m2
              kind: print
              publisher: Springer London
              date: "2008"
              ids:
                isbn:
                    - "9781848000049"
                    - "9781848000056"
      relations:
        - kind: part_of
          to: 3YXAC8SZBF
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.2 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4471-3655-2
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-84800-005-6
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
