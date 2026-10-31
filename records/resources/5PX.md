---
records:
    - id: 5PX46B1Z8S
      kind: monograph
      title: 'Complex Analysis I: Proceedings of the Special Year held at the University of Maryland, College Park, 1985–86'
      creators:
        - name: Carlos A. Berenstein
          role: editor
      date: "1987"
      expressions:
        - key: e1
          kind: edition
          date: "1987"
          ids:
            doi:
                - 10.1007/bfb0078339
                - 10.1007/bfb0078948
          manifestations:
            - key: m1
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "1987"
              ids:
                isbn:
                    - "9783540183563"
                    - "9783540478997"
            - key: m2
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "1987"
              ids:
                isbn:
                    - "9783540183570"
                    - "9783540479048"
      relations:
        - kind: part_of
          to: MYK049V6DA
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.4 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/bfb0078339
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/bfb0078948
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
