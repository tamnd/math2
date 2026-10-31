---
records:
    - id: 4MECY0CHS3
      kind: monograph
      title: General Topology II
      creators:
        - name: A. V. Arhangel’skii
          role: editor
      date: "1995"
      expressions:
        - key: e1
          kind: edition
          date: "1995"
          ids:
            doi:
                - 10.1007/978-3-642-77030-2
                - 10.1007/978-3-662-07413-8
          manifestations:
            - key: m1
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "1996"
              ids:
                isbn:
                    - "9783642770326"
                    - "9783642770302"
            - key: m2
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "1995"
              ids:
                isbn:
                    - "9783642081231"
                    - "9783662074138"
      relations:
        - kind: part_of
          to: XGZPMQ7BSM
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.4 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-3-642-77030-2
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-3-662-07413-8
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
