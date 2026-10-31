---
records:
    - id: NYRD0W2R6N
      kind: monograph
      title: Lectures in Abstract Algebra
      creators:
        - name: Nathan Jacobson
          role: author
      date: "1953"
      expressions:
        - key: e1
          kind: edition
          date: "1953"
          ids:
            doi:
                - 10.1007/978-1-4612-9872-4
                - 10.1007/978-1-4684-7053-6
          manifestations:
            - key: m1
              kind: print
              publisher: Springer New York
              date: "1964"
              ids:
                isbn:
                    - "9780387901244"
                    - "9781461298724"
            - key: m2
              kind: print
              publisher: Springer New York
              date: "1953"
              ids:
                isbn:
                    - "9781468470550"
                    - "9781468470536"
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
          native_id: 10.1007/978-1-4612-9872-4
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4684-7053-6
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
