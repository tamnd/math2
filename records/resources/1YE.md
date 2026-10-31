---
records:
    - id: 1YEB18HMGQ
      kind: monograph
      title: Graph Theory
      creators:
        - name: Ralucca Gera
          role: editor
        - name: Stephen Hedetniemi
          role: editor
        - name: Craig Larson
          role: editor
      date: "2016"
      expressions:
        - key: e1
          kind: edition
          date: "2016"
          ids:
            doi:
                - 10.1007/978-3-319-31940-7
                - 10.1007/978-3-319-97686-0
          manifestations:
            - key: m1
              kind: print
              publisher: Springer International Publishing
              date: "2016"
              ids:
                isbn:
                    - "9783319319384"
                    - "9783319319407"
            - key: m2
              kind: print
              publisher: Springer International Publishing
              date: "2018"
              ids:
                isbn:
                    - "9783319976846"
                    - "9783319976860"
      relations:
        - kind: part_of
          to: AQAR17SPHM
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.4 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-3-319-31940-7
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-3-319-97686-0
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
