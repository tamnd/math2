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
      msc:
        - code: 93-01
          from: zbmath_search
        - code: 93C20
          from: zbmath_search
        - code: 93C35
          from: zbmath_search
        - code: 93D05
          from: zbmath_search
        - code: 93D23
          from: zbmath_search
        - code: 93C05
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "2020"
          ids:
            doi: 10.1007/978-1-0716-0590-5
            zbl: "1459.93001"
            zbl_id: "7188322"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer New York
              date: "2020"
              ids:
                isbn:
                    - "9781071605882"
                    - "9781071605905"
              access:
                class: record
      relations:
        - kind: part_of
          to: 7B8JKAVW9F
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.13 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-0716-0590-5
          level: work
        - source: zbmath_search
          snapshot: blake3:a8e1c9c763cc4a7cf0816f17b1654f8f6ec07d6faeb609dc93b9b617c8b4e7e4
          native_id: "7188322"
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
      msc:
        - code: 65-XX
          from: arxiv
        - code: 49-XX
          from: arxiv
        - code: 90-XX
          from: arxiv
        - code: 93-XX
          from: arxiv
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
          language: en
          date: "2026-10-02"
          ids:
            arxiv: "2610.02983"
      scope:
        value: in
        rule: S1
        by: m2 v0.6.13 scope/1
      catalogue:
        - source: arxiv
          snapshot: blake3:e8374453dcab7bada88a6b850ab5bc0a0d87abd798991c12ac2d6c76ecd2c055
          native_id: "2610.02983"
          level: work
        - source: arxiv_text
          snapshot: blake3:b523016991566b44cacf0976b2dcb4dfca52ceb7fd07e311b05971173c8f0b4d
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
        - op: scope
          at: "2026-11-01"
          by: m2 v0.6.13 scope/1
          note: from in to in
---
