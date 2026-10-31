---
records:
    - id: QWBSYY1MP8
      kind: monograph
      title: Measure and Category
      creators:
        - name: John C. Oxtoby
          role: author
      date: "1971"
      expressions:
        - key: e1
          kind: edition
          date: "1971"
          ids:
            doi:
                - 10.1007/978-1-4615-9964-7
                - 10.1007/978-1-4684-9339-9
          manifestations:
            - key: m1
              kind: print
              publisher: Springer US
              date: "1971"
              ids:
                isbn:
                    - "9780387053493"
                    - "9781461599647"
            - key: m2
              kind: print
              publisher: Springer New York
              date: "1980"
              ids:
                isbn:
                    - "9781468493412"
                    - "9781468493399"
      relations:
        - kind: part_of
          to: 7ME1ABA6H5
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.7 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4615-9964-7
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4684-9339-9
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
