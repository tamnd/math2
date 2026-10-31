---
records:
    - id: HHA67BAZNV
      kind: monograph
      title: Introduction to Perturbation Methods
      creators:
        - name: Mark H. Holmes
          role: author
      date: "1995"
      expressions:
        - key: e1
          kind: edition
          date: "1995"
          ids:
            doi:
                - 10.1007/978-1-4612-5347-1
                - 10.1007/978-1-4614-5477-9
          manifestations:
            - key: m1
              kind: print
              publisher: Springer New York
              date: "1995"
              ids:
                isbn:
                    - "9781461253495"
                    - "9781461253471"
            - key: m2
              kind: print
              publisher: Springer New York
              date: "2013"
              ids:
                isbn:
                    - "9781461454762"
                    - "9781461454779"
      relations:
        - kind: part_of
          to: 7B8JKAVW9F
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.2 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4612-5347-1
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4614-5477-9
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
