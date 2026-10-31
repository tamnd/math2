---
records:
    - id: W4G7BCHYEW
      kind: preprint
      title: Sharp higher-order uncertainty principles
      creators:
        - name: Hongtao Hu
          role: author
        - name: Meiqi Liu
          role: author
        - name: Wenming Zou
          role: author
      date: "2026-10-01"
      subjects:
        - system: arxiv
          code: math.AP
      expressions:
        - key: e1
          kind: version
          label: preprint
          date: "2026-10-01"
          ids:
            arxiv: "2610.01561"
      catalogue:
        - source: arxiv
          snapshot: blake3:e8374453dcab7bada88a6b850ab5bc0a0d87abd798991c12ac2d6c76ecd2c055
          native_id: "2610.01561"
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.7 cluster/1
    - id: W4GFGPGYT8
      kind: monograph
      title: Introduction to Ring Theory
      creators:
        - name: P. M. Cohn
          role: author
      date: "2000"
      expressions:
        - key: e1
          kind: edition
          date: "2000"
          ids:
            doi: 10.1007/978-1-4471-0475-9
          manifestations:
            - key: m1
              kind: print
              publisher: Springer London
              date: "2000"
              ids:
                isbn:
                    - "9781852332068"
                    - "9781447104759"
      relations:
        - kind: part_of
          to: 3YXAC8SZBF
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.4 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4471-0475-9
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
