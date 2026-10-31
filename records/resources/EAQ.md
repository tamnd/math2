---
records:
    - id: EAQN8XZAD6
      kind: monograph
      title: Introduction to Elliptic Curves and Modular Forms
      creators:
        - name: Neal Koblitz
          role: author
      date: "1984"
      expressions:
        - key: e1
          kind: edition
          date: "1984"
          ids:
            doi:
                - 10.1007/978-1-4612-0909-6
                - 10.1007/978-1-4684-0255-1
          manifestations:
            - key: m1
              kind: print
              publisher: Springer New York
              date: "1993"
              ids:
                isbn:
                    - "9781461269427"
                    - "9781461209096"
            - key: m2
              kind: print
              publisher: Springer US
              date: "1984"
              ids:
                isbn:
                    - "9781468402575"
                    - "9781468402551"
      relations:
        - kind: part_of
          to: 7ME1ABA6H5
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.2 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4612-0909-6
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4684-0255-1
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
