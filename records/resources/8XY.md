---
records:
    - id: 8XYHY5E8JT
      kind: monograph
      title: A Course in Homological Algebra
      creators:
        - name: Peter J. Hilton
          role: author
        - name: Urs Stammbach
          role: author
      date: "1971"
      expressions:
        - key: e1
          kind: edition
          date: "1971"
          ids:
            doi:
                - 10.1007/978-1-4419-8566-8
                - 10.1007/978-1-4684-9936-0
          manifestations:
            - key: m1
              kind: print
              publisher: Springer New York
              date: "1997"
              ids:
                isbn:
                    - "9781461264385"
                    - "9781441985668"
            - key: m2
              kind: print
              publisher: Springer New York
              date: "1971"
              ids:
                isbn:
                    - "9780387900339"
                    - "9781468499360"
      relations:
        - kind: part_of
          to: 7ME1ABA6H5
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.4 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4419-8566-8
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4684-9936-0
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
