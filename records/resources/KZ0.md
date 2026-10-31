---
records:
    - id: KZ0JA8XNRB
      kind: monograph
      title: Bifurcation without Parameters
      creators:
        - name: Stefan Liebscher
          role: author
      date: "2015"
      expressions:
        - key: e1
          kind: edition
          date: "2015"
          ids:
            doi: 10.1007/978-3-319-10777-6
          manifestations:
            - key: m1
              kind: print
              publisher: Springer International Publishing
              date: "2015"
              ids:
                isbn:
                    - "9783319107769"
                    - "9783319107776"
      relations:
        - kind: part_of
          to: MYK049V6DA
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.7 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-3-319-10777-6
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
    - id: KZ0ZRYE0ZH
      kind: preprint
      title: Community Detection using the Edge Laplacian Dynamics vis-a-vis Ricci Flow
      creators:
        - name: Pratibha Bhandari
          role: author
        - name: Soumyendu Raha
          role: author
      date: "2026-09-30"
      subjects:
        - system: arxiv
          code: math.DS
        - system: arxiv
          code: cs.SI
      expressions:
        - key: e1
          kind: version
          label: preprint
          date: "2026-09-30"
          ids:
            arxiv: "2609.38988"
      scope:
        value: in
        rule: S2
        by: m2 v0.6.7 scope/1
      catalogue:
        - source: arxiv
          snapshot: blake3:e8374453dcab7bada88a6b850ab5bc0a0d87abd798991c12ac2d6c76ecd2c055
          native_id: "2609.38988"
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
