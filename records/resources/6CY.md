---
records:
    - id: 6CYZ8R76P3
      kind: monograph
      title: Algebraic K-Theory
      creators:
        - name: R. Keith Dennis
          role: editor
      date: "1982"
      expressions:
        - key: e1
          kind: edition
          date: "1982"
          ids:
            doi:
                - 10.1007/bfb0061896
                - 10.1007/bfb0062163
          manifestations:
            - key: m1
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "1982"
              ids:
                isbn:
                    - "9783540119661"
                    - "9783540395560"
            - key: m2
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "1982"
              ids:
                isbn:
                    - "9783540119654"
                    - "9783540395539"
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
          native_id: 10.1007/bfb0061896
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/bfb0062163
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
