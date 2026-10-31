---
records:
    - id: RSAWP7FD23
      kind: monograph
      title: 'Mathematical Problems in Image Processing: Partial Differential Equations and the Calculus of Variations'
      creators:
        - name: Gilles Aubert
          role: author
        - name: Pierre Kornprobst
          role: author
      date: "2002"
      expressions:
        - key: e1
          kind: edition
          date: "2002"
          ids:
            doi:
                - 10.1007/978-0-387-44588-5
                - 10.1007/b97428
          manifestations:
            - key: m1
              kind: print
              publisher: Springer New York
              date: "2006"
              ids:
                isbn:
                    - "9780387322001"
                    - "9780387445885"
            - key: m2
              kind: print
              publisher: Springer New York
              date: "2002"
              ids:
                isbn:
                    - "9780387953267"
                    - "9780387217666"
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
          native_id: 10.1007/978-0-387-44588-5
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/b97428
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
