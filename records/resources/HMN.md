---
records:
    - id: HMNDBRJWHZ
      kind: monograph
      title: 'Introduction to Infinite-Dimensional Systems Theory: A State-Space Approach'
      creators:
        - name: Ruth Curtain
          role: author
        - name: Hans Zwart
          role: author
      date: "2020"
      expressions:
        - key: e1
          kind: edition
          date: "2020"
          ids:
            doi: 10.1007/978-1-0716-0590-5
          manifestations:
            - key: m1
              kind: print
              publisher: Springer New York
              date: "2020"
              ids:
                isbn:
                    - "9781071605882"
                    - "9781071605905"
      relations:
        - kind: part_of
          to: 7B8JKAVW9F
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.7 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-0716-0590-5
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
    - id: HMNKENER22
      kind: preprint
      title: 'From Continuous to Fully Discrete Carleman Estimates: A Transfer Principle for Parabolic Schemes'
      creators:
        - name: Qi Lü
          role: author
        - name: Yu Wang
          role: author
      date: "2026-10-02"
      subjects:
        - system: arxiv
          code: math.NA
        - system: arxiv
          code: cs.NA
        - system: arxiv
          code: math.OC
      expressions:
        - key: e1
          kind: version
          label: preprint
          date: "2026-10-02"
          ids:
            arxiv: "2610.02983"
      scope:
        value: in
        rule: S2
        by: m2 v0.6.7 scope/1
      catalogue:
        - source: arxiv
          snapshot: blake3:e8374453dcab7bada88a6b850ab5bc0a0d87abd798991c12ac2d6c76ecd2c055
          native_id: "2610.02983"
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
