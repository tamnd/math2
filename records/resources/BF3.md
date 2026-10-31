---
records:
    - id: BF36J9417A
      kind: monograph
      title: Joins and Intersections
      creators:
        - name: Hubert Flenner
          role: author
        - name: Liam O’Carroll
          role: author
        - name: Wolfgang Vogel
          role: author
      date: "1999"
      expressions:
        - key: e1
          kind: edition
          date: "1999"
          ids:
            doi: 10.1007/978-3-662-03817-8
          manifestations:
            - key: m1
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "1999"
              ids:
                isbn:
                    - "9783642085628"
                    - "9783662038178"
      relations:
        - kind: part_of
          to: FA5PXCH6G7
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.2 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-3-662-03817-8
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
