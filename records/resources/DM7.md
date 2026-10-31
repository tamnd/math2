---
records:
    - id: DM7XS043AN
      kind: monograph
      title: Inverse Problems for Partial Differential Equations
      creators:
        - name: Victor Isakov
          role: author
      date: "1998"
      expressions:
        - key: e1
          kind: edition
          date: "1998"
          ids:
            doi:
                - 10.1007/978-1-4899-0030-2
                - 10.1007/978-3-319-51658-5
          manifestations:
            - key: m1
              kind: print
              publisher: Springer New York
              date: "1998"
              ids:
                isbn:
                    - "9781489900326"
                    - "9781489900302"
            - key: m2
              kind: print
              publisher: Springer International Publishing
              date: "2017"
              ids:
                isbn:
                    - "9783319516578"
                    - "9783319516585"
      relations:
        - kind: part_of
          to: 2M0N86YNGA
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.7 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4899-0030-2
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-3-319-51658-5
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
