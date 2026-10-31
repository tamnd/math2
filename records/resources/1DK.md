---
records:
    - id: 1DKYPR91S1
      kind: monograph
      title: The Arithmetic of Elliptic Curves
      creators:
        - name: Joseph H. Silverman
          role: author
      date: "1986"
      expressions:
        - key: e1
          kind: edition
          date: "1986"
          ids:
            doi:
                - 10.1007/978-0-387-09494-6
                - 10.1007/978-1-4757-1920-8
          manifestations:
            - key: m1
              kind: print
              publisher: Springer New York
              date: "2009"
              ids:
                isbn:
                    - "9780387094939"
                    - "9780387094946"
            - key: m2
              kind: print
              publisher: Springer New York
              date: "1986"
              ids:
                isbn:
                    - "9781475719222"
                    - "9781475719208"
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
          native_id: 10.1007/978-0-387-09494-6
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4757-1920-8
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
