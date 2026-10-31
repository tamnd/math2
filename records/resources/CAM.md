---
records:
    - id: CAM5RRFGYW
      kind: monograph
      title: 'Modular Forms: Basics and Beyond'
      creators:
        - name: Goro Shimura
          role: author
      date: "2012"
      expressions:
        - key: e1
          kind: edition
          date: "2012"
          ids:
            doi: 10.1007/978-1-4614-2125-2
          manifestations:
            - key: m1
              kind: print
              publisher: Springer New York
              date: "2012"
              ids:
                isbn:
                    - "9781461421245"
                    - "9781461421252"
      relations:
        - kind: part_of
          to: FA5PXCH6G7
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.4 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4614-2125-2
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
    - id: CAMS0T9GRF
      kind: preprint
      title: Learning Closure of Dynamical Systems with Kernel Ridge Regression
      creators:
        - name: Evan Habbershaw
          role: author
        - name: John Harlim
          role: author
        - name: Senwei Liang
          role: author
      date: "2026-10-01"
      subjects:
        - system: arxiv
          code: math.NA
        - system: arxiv
          code: cs.LG
        - system: arxiv
          code: cs.NA
        - system: arxiv
          code: math.DS
      expressions:
        - key: e1
          kind: version
          label: preprint
          date: "2026-10-01"
          ids:
            arxiv: "2610.02564"
      catalogue:
        - source: arxiv
          snapshot: blake3:e8374453dcab7bada88a6b850ab5bc0a0d87abd798991c12ac2d6c76ecd2c055
          native_id: "2610.02564"
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.7 cluster/1
---
