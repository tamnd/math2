---
records:
    - id: FZ7XKXJ2VP
      kind: monograph
      title: Mathematical Tapas
      creators:
        - name: Jean-Baptiste Hiriart-Urruty
          role: author
      date: "2016"
      expressions:
        - key: e1
          kind: edition
          date: "2016"
          ids:
            doi:
                - 10.1007/978-3-319-42186-5
                - 10.1007/978-3-319-68631-8
          manifestations:
            - key: m1
              kind: print
              publisher: Springer International Publishing
              date: "2016"
              ids:
                isbn:
                    - "9783319421858"
                    - "9783319421865"
              access:
                class: record
            - key: m2
              kind: print
              publisher: Springer International Publishing
              date: "2017"
              ids:
                isbn:
                    - "9783319686301"
                    - "9783319686318"
              access:
                class: record
      relations:
        - kind: part_of
          to: 3YXAC8SZBF
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.14 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-3-319-42186-5
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-3-319-68631-8
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
