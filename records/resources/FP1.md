---
records:
    - id: FP1069RB4H
      kind: monograph
      title: A Hilbert Space Problem Book
      creators:
        - name: P. R. Halmos
          role: author
      date: "1974"
      expressions:
        - key: e1
          kind: edition
          date: "1974"
          ids:
            doi:
                - 10.1007/978-1-4615-9976-0
                - 10.1007/978-1-4684-9330-6
          manifestations:
            - key: m1
              kind: print
              publisher: Springer US
              date: "1974"
              ids:
                isbn:
                    - "9781461599784"
                    - "9781461599760"
            - key: m2
              kind: print
              publisher: Springer New York
              date: "1982"
              ids:
                isbn:
                    - "9781468493320"
                    - "9781468493306"
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
          native_id: 10.1007/978-1-4615-9976-0
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4684-9330-6
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
