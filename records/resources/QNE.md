---
records:
    - id: QNE8Y1E3EZ
      kind: monograph
      title: Introduction to Smooth Manifolds
      creators:
        - name: John M. Lee
          role: author
      date: "2003"
      expressions:
        - key: e1
          kind: edition
          date: "2003"
          ids:
            doi:
                - 10.1007/978-0-387-21752-9
                - 10.1007/978-1-4419-9982-5
          manifestations:
            - key: m1
              kind: print
              publisher: Springer New York
              date: "2003"
              ids:
                isbn:
                    - "9780387954486"
                    - "9780387217529"
            - key: m2
              kind: print
              publisher: Springer New York
              date: "2012"
              ids:
                isbn:
                    - "9781441999818"
                    - "9781441999825"
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
          native_id: 10.1007/978-0-387-21752-9
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4419-9982-5
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
