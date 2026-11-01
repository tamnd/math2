---
records:
    - id: ZTREM09NFT
      kind: preprint
      title: Computing Extinction Barriers in a Quorum-Sensing Reaction Network
      creators:
        - name: Mario Ayala
          role: author
        - name: Johannes Zimmer
          role: author
      date: "2026-09-30"
      msc:
        - code: 60-XX
          from: arxiv
        - code: 65-XX
          from: arxiv
      subjects:
        - system: arxiv
          code: math.PR
        - system: arxiv
          code: cond-mat.stat-mech
        - system: arxiv
          code: cs.NA
        - system: arxiv
          code: math.NA
        - system: arxiv
          code: q-bio.PE
      expressions:
        - key: e1
          kind: version
          label: preprint
          language: en
          date: "2026-09-30"
          ids:
            arxiv: "2609.39946"
            zbl_id: "903192129"
      scope:
        value: in
        rule: S1
        by: m2 v0.6.13 scope/1
      catalogue:
        - source: arxiv
          snapshot: blake3:e8374453dcab7bada88a6b850ab5bc0a0d87abd798991c12ac2d6c76ecd2c055
          native_id: "2609.39946"
          level: work
        - source: arxiv_text
          snapshot: blake3:b523016991566b44cacf0976b2dcb4dfca52ceb7fd07e311b05971173c8f0b4d
          native_id: "2609.39946"
          level: work
        - source: zbmath_search
          snapshot: blake3:a8e1c9c763cc4a7cf0816f17b1654f8f6ec07d6faeb609dc93b9b617c8b4e7e4
          native_id: "903192129"
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
    - id: ZTRKX4B0FG
      kind: monograph
      title: Graph Theory
      creators:
        - name: Béla Bollobás
          role: author
      date: "1979"
      msc:
        - code: 05Cxx
          from: zbmath_search
        - code: 05-01
          from: zbmath_search
        - code: 94C30
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "1979"
          ids:
            doi: 10.1007/978-1-4612-9967-7
            zbl: "0411.05032"
            zbl_id: "3637904"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer New York
              date: "1979"
              ids:
                isbn:
                    - "9781461299691"
                    - "9781461299677"
              access:
                class: record
      relations:
        - kind: part_of
          to: 7ME1ABA6H5
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 v0.6.13 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4612-9967-7
          level: work
        - source: zbmath_search
          snapshot: blake3:a8e1c9c763cc4a7cf0816f17b1654f8f6ec07d6faeb609dc93b9b617c8b4e7e4
          native_id: "3637904"
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
