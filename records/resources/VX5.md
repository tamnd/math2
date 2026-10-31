---
records:
    - id: VX52BJ1X4H
      kind: monograph
      title: Inverse Galois Theory
      creators:
        - name: Gunter Malle
          role: author
        - name: B. Heinrich Matzat
          role: author
      date: "1999"
      expressions:
        - key: e1
          kind: edition
          date: "1999"
          ids:
            doi:
                - 10.1007/978-3-662-12123-8
                - 10.1007/978-3-662-55420-3
          manifestations:
            - key: m1
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "1999"
              ids:
                isbn:
                    - "9783642083112"
                    - "9783662121238"
            - key: m2
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "2018"
              ids:
                isbn:
                    - "9783662554197"
                    - "9783662554203"
      relations:
        - kind: part_of
          to: FA5PXCH6G7
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.2 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-3-662-12123-8
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-3-662-55420-3
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
