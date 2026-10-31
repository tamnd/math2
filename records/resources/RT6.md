---
records:
    - id: RT6DDTXMKJ
      kind: monograph
      title: Postmodern Analysis
      creators:
        - name: Jürgen Jost
          role: author
      date: "1998"
      expressions:
        - key: e1
          kind: edition
          date: "1998"
          ids:
            doi:
                - 10.1007/978-3-662-03635-8
                - 10.1007/978-3-662-05306-5
          manifestations:
            - key: m1
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "1998"
              ids:
                isbn:
                    - "9783540634850"
                    - "9783662036358"
            - key: m2
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "2003"
              ids:
                isbn:
                    - "9783540438731"
                    - "9783662053065"
      relations:
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
          native_id: 10.1007/978-3-662-03635-8
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-3-662-05306-5
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
