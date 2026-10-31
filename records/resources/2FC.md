---
records:
    - id: 2FC3WXY33P
      kind: edited-volume
      title: 'Algebraic Topology: Oaxtepec 1991'
      creators:
        - name: Martin C. Tangora
          role: editor
      date: "1993"
      expressions:
        - key: e1
          kind: edition
          date: "1993"
          ids:
            doi: 10.1090/conm/146
          manifestations:
            - key: m1
              kind: print
              publisher: American Mathematical Society
              date: "1993"
              ids:
                isbn:
                    - "9780821851623"
                    - "9780821854808"
                    - "9780821877371"
      relations:
        - kind: part_of
          to: VAEN3CBGT1
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.7 scope/1
      catalogue:
        - source: ams-series
          snapshot: blake3:caf23f13a44130cfaf0ea65e08f1b670683c2f34af9ccb44343f3bca428b1013
          native_id: 10.1090/conm/146
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
    - id: 2FCSSBRX80
      kind: preprint
      title: 'Certified machine learning: A posteriori error estimation for physics-informed neural networks'
      creators:
        - name: Birgit Hillebrecht
          role: author
        - name: Benjamin Unger
          role: author
      date: "2022-03-31"
      subjects:
        - system: arxiv
          code: cs.LG
        - system: arxiv
          code: cs.NA
        - system: arxiv
          code: math.NA
      expressions:
        - key: e1
          kind: version
          label: preprint
          date: "2022-03-31"
          ids:
            arxiv: "2203.17055"
            doi: 10.1109/ijcnn55064.2022.9892569
      scope:
        value: border
        rule: border-arxiv
        by: m2 v0.6.7 scope/1
      catalogue:
        - source: arxiv
          snapshot: blake3:e8374453dcab7bada88a6b850ab5bc0a0d87abd798991c12ac2d6c76ecd2c055
          native_id: "2203.17055"
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.7 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.7 scope/1
          note: to border
---
