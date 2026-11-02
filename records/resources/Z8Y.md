---
records:
    - id: Z8Y5DZPRZT
      kind: monograph
      title: 'Exercises in Analysis: Part 1'
      creators:
        - name: Leszek Gasińksi
          role: author
        - name: Nikolaos S. Papageorgiou
          role: author
      date: "2014"
      msc:
        - code: 00A07
          from: zbmath_search
        - code: 26-01
          from: zbmath_search
        - code: 54-01
          from: zbmath_search
        - code: 46-01
          from: zbmath_search
        - code: 28-01
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "2014"
          ids:
            doi: 10.1007/978-3-319-06176-4
            zbl: "1298.00007"
            zbl_id: "6292872"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer International Publishing
              date: "2014"
              ids:
                isbn:
                    - "9783319061757"
                    - "9783319061764"
              access:
                class: record
      relations:
        - kind: part_of
          to: AQAR17SPHM
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 dev scope/1
      catalogue:
        - source: crossref_language
          snapshot: blake3:99510ada1a0f54f83dbf4ed97ef48852461d1f98d338d1a350cabf222fb85948
          native_id: 10.1007/978-3-319-06176-4
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-3-319-06176-4
          level: work
        - source: zbmath_search
          snapshot: blake3:25dd7c4358839cf7c8c9f5d07f0562e94f38728153e7db2255a7191282b967c2
          native_id: "6292872"
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
          at: "2026-11-02"
          by: m2 dev scope/1
          note: from in to in
---
