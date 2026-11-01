---
records:
    - id: 9KZF1NFT7G
      kind: monograph
      title: Proceedings of Liverpool Singularities — Symposium I
      creators:
        - name: C.T.C. Wall
          role: editor
      date: "1971"
      msc:
        - code: 00B25
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "1971"
          ids:
            doi:
                - 10.1007/bfb0066809
                - 10.1007/bfb0068889
            zbl: "0211.00202"
            zbl_id: "3334125"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "1971"
              ids:
                isbn:
                    - "9783540054023"
                    - "9783540365310"
              access:
                class: record
            - key: m2
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "1971"
              ids:
                isbn:
                    - "9783540055112"
                    - "9783540368687"
              access:
                class: record
      relations:
        - kind: part_of
          to: MYK049V6DA
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 v0.6.16 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/bfb0066809
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/bfb0068889
          level: work
        - source: zbmath_search
          snapshot: blake3:928c873c1dac6852b2bf2c77184182759305f81342a4dc8ca5c0d4768bc6dd1e
          native_id: "3334125"
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
        - op: scope
          at: "2026-11-01"
          by: m2 v0.6.14 scope/1
          note: from in to in
---
