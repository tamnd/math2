---
records:
    - id: 8JDQ9FWFRK
      kind: preprint
      title: 'Optimal detection of general moment changes: Simultaneous mean and covariance change detection and beyond'
      creators:
        - name: Xiaokai Luo
          role: author
        - name: Chenghao Xu
          role: author
        - name: Haotian Xu
          role: author
        - name: Carlos Misael Madrid Padilla
          role: author
        - name: Daren Wang
          role: author
      date: "2026-09-29"
      subjects:
        - system: arxiv
          code: stat.ME
        - system: arxiv
          code: math.ST
        - system: arxiv
          code: stat.ML
        - system: arxiv
          code: stat.TH
      expressions:
        - key: e1
          kind: version
          label: preprint
          date: "2026-09-29"
          ids:
            arxiv: "2609.36594"
      scope:
        value: border
        rule: border-arxiv
        by: m2 v0.6.13 scope/1
      catalogue:
        - source: arxiv
          snapshot: blake3:e8374453dcab7bada88a6b850ab5bc0a0d87abd798991c12ac2d6c76ecd2c055
          native_id: "2609.36594"
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.7 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.7 scope/1
          note: to border
    - id: 8JDXWZM0RN
      kind: problem-set
      title: BMO Round 1 2000
      creators:
        - name: UK Mathematics Trust
          role: author
      date: "2000-01-12"
      msc:
        - code: 00A07
          from: bmo
        - code: 97U40
          from: bmo
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "2000-01-12"
          structure: 8JDXWZM0RN/e1.json
      relations:
        - kind: part_of
          to: 8XFPR5H74Q
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 v0.6.13 scope/1
      catalogue:
        - source: bmo
          snapshot: blake3:68eb2251465334659a3c67c12bc8e13877594a5a11510cf9a756eaf0f62db81c
          native_id: bmo1-2000
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
          by: m2 v0.6.13 scope/1
          note: from in to in
---
