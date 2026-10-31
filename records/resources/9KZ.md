---
records:
    - id: 9KZF1NFT7G
      kind: monograph
      title: Proceedings of Liverpool Singularities — Symposium I
      creators:
        - name: C.T.C. Wall
          role: editor
      date: "1971"
      expressions:
        - key: e1
          kind: edition
          date: "1971"
          ids:
            doi:
                - 10.1007/bfb0066809
                - 10.1007/bfb0068889
          manifestations:
            - key: m1
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "1971"
              ids:
                isbn:
                    - "9783540054023"
                    - "9783540365310"
            - key: m2
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "1971"
              ids:
                isbn:
                    - "9783540055112"
                    - "9783540368687"
      relations:
        - kind: part_of
          to: MYK049V6DA
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.4 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/bfb0066809
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/bfb0068889
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
