---
records:
    - id: V7W1TQ92CG
      kind: monograph
      title: Second Order Equations of Elliptic and Parabolic Type
      creators:
        - name: E. Landis
          role: author
      date: "1997-12-02"
      expressions:
        - key: e1
          kind: edition
          date: "1997-12-02"
          ids:
            doi: 10.1090/mmono/171
          manifestations:
            - key: m1
              kind: print
              publisher: American Mathematical Society
              date: "1997-12-02"
              ids:
                isbn:
                    - "9780821808573"
                    - "9780821897812"
                    - "9781470445867"
      relations:
        - kind: part_of
          to: BTDY0N3WC9
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.7 scope/1
      catalogue:
        - source: ams-series
          snapshot: blake3:caf23f13a44130cfaf0ea65e08f1b670683c2f34af9ccb44343f3bca428b1013
          native_id: 10.1090/mmono/171
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
    - id: V7WT21EDPM
      kind: preprint
      title: The optimal information complexity of VC learning
      creators:
        - name: Steve Hanneke
          role: author
        - name: Juexiao Wang
          role: author
      date: "2026-10-06"
      subjects:
        - system: arxiv
          code: stat.ML
        - system: arxiv
          code: cs.IT
        - system: arxiv
          code: cs.LG
        - system: arxiv
          code: math.IT
        - system: arxiv
          code: math.ST
        - system: arxiv
          code: stat.TH
      expressions:
        - key: e1
          kind: version
          label: preprint
          date: "2026-10-06"
          ids:
            arxiv: "2610.10600"
      scope:
        value: border
        rule: border-arxiv
        by: m2 v0.6.7 scope/1
      catalogue:
        - source: arxiv
          snapshot: blake3:e8374453dcab7bada88a6b850ab5bc0a0d87abd798991c12ac2d6c76ecd2c055
          native_id: "2610.10600"
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
