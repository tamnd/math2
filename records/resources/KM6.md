---
records:
    - id: KM6AGC23YY
      kind: edited-volume
      title: Tropical and Non-Archimedean Geometry
      creators:
        - name: Omid Amini
          role: editor
        - name: Matthew Baker
          role: editor
        - name: Xander Faber
          role: editor
      date: "2013-12-26"
      expressions:
        - key: e1
          kind: edition
          date: "2013-12-26"
          ids:
            doi: 10.1090/conm/605
          manifestations:
            - key: m1
              kind: print
              publisher: American Mathematical Society
              date: "2013-12-26"
              ids:
                isbn:
                    - "9781470410216"
                    - "9781470414108"
                    - "9781470414153"
      relations:
        - kind: part_of
          to: VAEN3CBGT1
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.4 scope/1
      catalogue:
        - source: ams-series
          snapshot: blake3:caf23f13a44130cfaf0ea65e08f1b670683c2f34af9ccb44343f3bca428b1013
          native_id: 10.1090/conm/605
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
    - id: KM6PX54YFZ
      kind: preprint
      title: Continuous-Time Trajectory Generation from Discrete Observations with Stochasticity
      creators:
        - name: Ruifeng Shang
          role: author
        - name: Shu Liu
          role: author
        - name: Yuhua Zhu
          role: author
      date: "2026-09-25"
      subjects:
        - system: arxiv
          code: stat.ML
        - system: arxiv
          code: cs.LG
        - system: arxiv
          code: math.DS
      expressions:
        - key: e1
          kind: version
          label: preprint
          date: "2026-09-25"
          ids:
            arxiv: "2609.32026"
      catalogue:
        - source: arxiv
          snapshot: blake3:e8374453dcab7bada88a6b850ab5bc0a0d87abd798991c12ac2d6c76ecd2c055
          native_id: "2609.32026"
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.7 cluster/1
---
