---
records:
    - id: JV2PV9J7JN
      kind: monograph
      title: 'Geometric Methods and Applications: For Computer Science and Engineering'
      creators:
        - name: Jean Gallier
          role: author
      date: "2001"
      expressions:
        - key: e1
          kind: edition
          date: "2001"
          ids:
            doi:
                - 10.1007/978-1-4419-9961-0
                - 10.1007/978-1-4613-0137-0
          manifestations:
            - key: m1
              kind: print
              publisher: Springer New York
              date: "2011"
              ids:
                isbn:
                    - "9781441999603"
                    - "9781441999610"
            - key: m2
              kind: print
              publisher: Springer New York
              date: "2001"
              ids:
                isbn:
                    - "9781461265092"
                    - "9781461301370"
      relations:
        - kind: part_of
          to: 7B8JKAVW9F
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.4 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4419-9961-0
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4613-0137-0
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
