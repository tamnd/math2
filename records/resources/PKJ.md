---
records:
    - id: PKJ36E74PZ
      kind: problem-set
      title: IMO 2020
      creators:
        - name: IMO Problem Selection Committee
          role: author
      date: "2020"
      msc:
        - code: 00A07
          from: imo
        - code: 97U40
          from: imo
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "2020"
      relations:
        - kind: part_of
          to: 931689K6X2
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 v0.6.14 scope/1
      catalogue:
        - source: imo
          snapshot: blake3:c564548c1a7c5bfe4e71cf81d61c599a9d4016d698feff8fb0bc9beb0e2f88f9
          native_id: "2020"
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
    - id: PKJFZEY8ZV
      kind: preprint
      title: Certain Family of Some Beta Distributions Arising from Distribution of Randomly Weighted Average
      creators:
        - name: Rasool Roozegar
          role: author
      date: "2015-08-07"
      msc:
        - code: 62-XX
          from: arxiv
      subjects:
        - system: arxiv
          code: math.ST
        - system: arxiv
          code: stat.TH
      expressions:
        - key: e1
          kind: version
          label: preprint
          language: en
          date: "2015-08-07"
          ids:
            arxiv: "1508.01731"
      scope:
        value: in
        rule: S2
        by: m2 v0.6.14 scope/1
      catalogue:
        - source: arxiv
          snapshot: blake3:e8374453dcab7bada88a6b850ab5bc0a0d87abd798991c12ac2d6c76ecd2c055
          native_id: "1508.01731"
          level: work
        - source: arxiv_text
          snapshot: blake3:b523016991566b44cacf0976b2dcb4dfca52ceb7fd07e311b05971173c8f0b4d
          native_id: "1508.01731"
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.7 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.7 scope/1
          note: to in
---
