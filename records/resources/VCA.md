---
records:
    - id: VCAJG7EEAH
      kind: monograph
      title: A Mathematical Introduction to Fluid Mechanics
      creators:
        - name: Alexandre J. Chorin
          role: author
        - name: Jerrold E. Marsden
          role: author
      date: "1979"
      expressions:
        - key: e1
          kind: edition
          date: "1979"
          ids:
            doi:
                - 10.1007/978-1-4612-0883-9
                - 10.1007/978-1-4684-0082-3
                - 10.1007/978-1-4684-0364-0
          manifestations:
            - key: m1
              kind: print
              publisher: Springer New York
              date: "1993"
              ids:
                isbn:
                    - "9781461269342"
                    - "9781461208839"
            - key: m2
              kind: print
              publisher: Springer US
              date: "1979"
              ids:
                isbn:
                    - "9780387904061"
                    - "9781468400823"
            - key: m3
              kind: print
              publisher: Springer US
              date: "1990"
              ids:
                isbn:
                    - "9781468403664"
                    - "9781468403640"
      relations:
        - kind: part_of
          to: 7B8JKAVW9F
          source: cluster/1
        - kind: part_of
          to: W0CC03QJC7
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.4 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4612-0883-9
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4684-0082-3
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4684-0364-0
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
